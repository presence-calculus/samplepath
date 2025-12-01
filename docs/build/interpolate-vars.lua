-- interpolate-vars.lua
--
-- Expands $var references using top-level metadata keys.
-- Example:
--   document-root: "../.."
--   header-image: "$document-root/assets/foo.png"
--   ...
--   ![Img]($document-root/examples/foo.png)
--
-- becomes "../..../assets/foo.png" and "../..../examples/foo.png"
-- in the generated HTML.

local vars = {}

-- Substitute $var tokens in a string using the vars table.
-- Matches $document-root, $title, $project_name, etc.
local function substitute(s)
  if type(s) ~= "string" then
    return s
  end

  -- %$([%w_%-]+) means:
  --   literal "$" followed by one or more of [A–Z a–z 0–9 _ -]
  return (s:gsub("%$([%w_%-]+)", function(key)
    -- If we don't know this var, leave it as-is
    return vars[key] or ("$" .. key)
  end))
end

-- Recursively walk metadata and apply substitution
local function transform_meta(x)
  if type(x) == "string" then
    return substitute(x)
  elseif type(x) == "table" then
    if x.t == "MetaString" then
      return pandoc.MetaString(substitute(x.text))
    elseif x.t == "MetaInlines" then
      -- turn MetaInlines into plain string, then re-wrap
      local txt = pandoc.utils.stringify(x)
      return pandoc.MetaString(substitute(txt))
    else
      local out = {}
      for k, v in pairs(x) do
        out[k] = transform_meta(v)
      end
      return out
    end
  else
    return x
  end
end

local function transform_inline(el)
  if el.t == "Str" then
    el.text = substitute(el.text)
    return el

  elseif el.t == "Code" then
    el.text = substitute(el.text)
    return el

  elseif el.t == "Link" then
    el.target = substitute(el.target)
    return el

  elseif el.t == "Image" then
    el.src = substitute(el.src)
    return el

  elseif el.t == "RawInline" and el.format == "html" then
    el.text = substitute(el.text)
    return el
  end

  return el
end

function Pandoc(doc)
  -- 1. Build vars from top-level metadata (as strings)
  for k, v in pairs(doc.meta) do
    vars[k] = pandoc.utils.stringify(v)
  end

  -- 2. Apply substitution inside metadata so templates see expanded values
  doc.meta = transform_meta(doc.meta)

  -- 3. Walk all inlines in the document (links, images, text)
  doc = doc:walk({
    Inline = transform_inline,
  })

  return doc
end
