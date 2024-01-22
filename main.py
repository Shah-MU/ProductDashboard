import streamlit as st
import pandas as pd
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid import AgGrid, GridUpdateMode
# custom
import scraperLib


# Title(s):
st.title("Product Scraper Dashboard")

# Streamlit UI

product_name = st.sidebar.text_input("Enter the product name:")
num_items = st.sidebar.number_input("Enter the number of items:", min_value=1, value=10)

if st.button("Scrape Products"):
    product_df = scraperLib.scrape_bestbuy_products(product_name, num_items)

    # Save DataFrame locally
    product_df.to_csv('scraped_data.csv', index=False)

# Load DataFrame from the saved CSV file
loaded_df = pd.read_csv('scraped_data.csv') if st.checkbox('Load saved data', True) else pd.DataFrame()

# AgGrid configuration
gd = GridOptionsBuilder.from_dataframe(loaded_df)
gd.configure_selection(selection_mode='single',pre_selected_rows=[0], use_checkbox=True)
gd.configure_column('Image URL', hide=True)  # Assuming 'image' is the column name for Image URL
grid_options = gd.build()


# Subheader(s):

st.write('## Select An Item To View')

# Configuring Columns:

col1, col2 = st.columns(2)


with col1:
    # Display AgGrid
    grid_table = AgGrid(loaded_df, height=250, gridOptions=grid_options, update_mode=GridUpdateMode.SELECTION_CHANGED)

# correction

if grid_table['selected_rows']:
    selected_row = grid_table['selected_rows'][0]
    selected_product_name = selected_row['Product Name']
    selected_image_url = selected_row['Image URL']
    selected_product_price = selected_row['Price']

# correction

selected_row = None

if not grid_table['selected_rows']:
        st.info('Select a product to view more info.')

if grid_table['selected_rows']:
    selected_row = grid_table['selected_rows'][0]
    image_column, description_column = st.columns(2)

with col2:

    if not selected_row == None:
        st.image(selected_row['Image URL'], caption='Selected Image', use_column_width=True)





