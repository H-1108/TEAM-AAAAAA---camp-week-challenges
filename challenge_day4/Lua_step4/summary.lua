-- Create a Metatable for summary merging
SummaryMetaTable = {
    __add = function (left, right)
        local newSummary = {super=0, good=0, middle=0, low=0}
        for k, v in pairs(left) do
            newSummary[k] = v + right[k]
        end
        return newSummary
    end
}

-- Read data from data4.txt (relative to project root)
local lines = {}
for line in io.lines("challenge_day4/testdata/data4.txt") do
    -- Optional: print("Reading line: " .. line)
    table.insert(lines, line)
end

-- Skip header
table.remove(lines, 1)

-- Initialize table to hold results
local people = {}

-- Process each person's skills
for _, line in ipairs(lines) do
    local name, tech, soft, bus, creative, academic =
        line:match("([^,]+),([^,]+),([^,]+),([^,]+),([^,]+),([^,]+)")
    
    local summary = {super=0, good=0, middle=0, low=0}
    setmetatable(summary, SummaryMetaTable)

    -- Count the skill levels
    for _, skill in ipairs({tech, soft, bus, creative, academic}) do
        summary[skill] = (summary[skill] or 0) + 1
    end

    -- Determine final summary level
    local finalSummary
    if summary.super > 0 then
        finalSummary = "super"
    elseif summary.good >= 2 then
        finalSummary = "good"
    elseif summary.middle >= 3 then
        finalSummary = "middle"
    else
        finalSummary = "low"
    end

    -- Save results
    table.insert(people, {name, tech, soft, bus, creative, academic, finalSummary})
end

-- Write results to challenge_day4/Lua_step4/data5.txt
local out = io.open("challenge_day4/Lua_step4/data5.txt", "w")
out:write("Name,Technical Skills,Soft Skills,Business Skills,Creative Skills,Academic Skills,Summary\n")
for _, entry in ipairs(people) do
    out:write(table.concat(entry, ',') .. "\n")
end
out:close()