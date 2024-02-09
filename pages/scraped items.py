import streamlit as st


# Title
st.title('Shopping List')

# Initialize the shopping list as an empty list
if 'shopping_list' not in st.session_state:
    st.session_state.shopping_list = []

# Text input to add items to the shopping list
new_item = st.text_input('Add item to the list:', '')

# Button to add the item to the shopping list
if st.button('Add', key='add_button'):
    if new_item.strip():  # Check if the input is not empty
        st.session_state.shopping_list.append(new_item)
        new_item = ''  # Clear the input field after adding the item

# Display the current shopping list
st.write('### Shopping List:')
if st.session_state.shopping_list:
    for idx, item in enumerate(st.session_state.shopping_list, start=1):
        st.write(f"{idx}. {item}")
else:
    st.write('Your shopping list is empty.')
    
# Button to remove the item from the shopping list
if st.button('Remove', key='remove_button'):
    if st.session_state.shopping_list:  # Check if the shopping list is not empty
        removed_item = st.session_state.shopping_list.pop(idx - 1)
        st.write(f"Removed: {removed_item}")

# Button to clear the shopping list
if st.button('Clear List', key='clear_button'):
    st.session_state.shopping_list = []
    new_item = ''  # Clear the input field after clearing the list