# Reflection on Data Cleaning Project

## What Copilot Generated
GitHub Copilot helped generate several of the core functions in my data cleaning script, including `load_data`, `clean_column_names`, `handle_missing_values`, and `remove_invalid_rows`. Copilot provided the initial function structure and suggested code for handling missing values and standardizing column names. These suggestions gave me a strong starting point and allowed me to focus on tailoring the logic specifically to the messy sales dataset I was working with. Without Copilot, writing these functions from scratch would have taken more time and required more trial and error.

## What I Modified
While Copilot’s suggestions were helpful, I made several important modifications to ensure the code met the assignment requirements and handled edge cases. For example, I added median imputation for missing numeric values, explicitly removed duplicate rows, and included detailed comments explaining each step. I also refined the column-cleaning function to consistently lowercase names and replace spaces with underscores. These modifications ensured the code not only worked correctly but was also clear and professional, ready to show on GitHub or a resume.

## What I Learned
This project taught me how to clean data in Python without relying solely on pandas, and how to integrate Copilot effectively into my workflow. I learned that AI-generated code is a helpful starting point but still requires human judgment, especially when dealing with edge cases or project-specific requirements. Additionally, I improved my ability to write clear comments and document each step of a data cleaning process. Overall, I gained practical skills in both Python programming and responsible AI-assisted coding, which will be valuable for future data projects.
