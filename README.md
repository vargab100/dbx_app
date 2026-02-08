# dbx_app
# Sync the files
1) Copy the template to your computer (skip this step if not using a template) --> databricks workspace export-dir <code_location_from_databricks> .
# Sync future edits back to Databricks
2) databricks sync --watch . <code_location_from_databricks>
# Run the app on your computer
3) Start the app --> python app.py
# And open the URL on the screen. For Streamlit apps, run 
4) streamlit run app.py
# Deploy to Databricks Apps
5) databricks apps deploy hello-world --source-code-path <code_location_from_databricks>
