import main

product_name = main.st.sidebar.text_input("Enter the product name:")

if 'shopping_list' not in main.st.session_state:
    main.st.session_state.shopping_list = []

# Button to add the item to the shopping list
if main.st.sidebar.button('Search', key = "add_button"):
    if main.product_name.strip():  # Check if the input is not empty
        main.st.session_state.shopping_list.append(main.product_name)
        new_item = ''  # Clear the input field after adding the item
        

# Display the current shopping list
if main.st.session_state.shopping_list:
    for idx, item in enumerate(main.st.session_state.shopping_list, start=1):
        main.st.sidebar.write(f"{idx}. {item}")
        
# Button to remove the item from the shopping list
if main.st.sidebar.button('Remove', key='remove_button'):
    if main.st.session_state.shopping_list:  # Check if the shopping list is not empty
        removed_item = main.st.session_state.shopping_list.pop(idx - 1)
        main.st.write(f"Removed: {removed_item}")