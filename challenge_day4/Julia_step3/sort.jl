using CSV, DataFrames, Statistics

# Load CSV
using CSV, DataFrames

people_df = DataFrame(
    CSV.File(joinpath(@__DIR__, "..", "fulldata", "data3.csv"))
)


# Function to classify a score based on quartiles
function classify_score(score, quartiles)
    if score <= quartiles[1]
        return "low"
    elseif score <= quartiles[2]
        return "middle"
    elseif score <= quartiles[3]
        return "good"
    else
        return "super"
    end
end

# Iterate over each column (skip 'name')
for col_name in names(people_df)[2:end]
    # Convert floats that are whole numbers to integers
    col_data = map(x -> isa(x, Float64) && x == floor(x) ? Int(x) : x, people_df[!, col_name])

    # Keep only integers for quartiles
    valid_data = filter(x -> x isa Int, col_data)

    if isempty(valid_data)
        println("No valid data for column $col_name")
        continue
    end

    quartiles = quantile(collect(Float64.(valid_data)), [0.25, 0.5, 0.75])

    # Map values to categories
    new_col = map(x -> x isa Float64 ? "low" : classify_score(x, quartiles), col_data)
    people_df[!, col_name] = new_col
end

# Save the modified DataFrame
CSV.write(joinpath(@__DIR__, "..", "..", "..", "fulldata", "data4.csv"), people_df)



