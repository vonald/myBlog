import datetime
from pathlib import Path


# Create date variables for use later
today = datetime.datetime.now( )
todays_date = today.strftime('%Y-%m-%d')
title_date = today.strftime('%d/%m/%Y')
todays_file = (todays_date+'.md')
print(todays_file)

# Read contents of draft file
with open('hugoDraft.md', 'r', ) as f:
        content = f.read()
        print(content)

# Check to see if todays file exists
folder_path_str = '/storage/emulated/0/Documents/markor/myBlog/content/posts/'
file_name = (todays_file)

# Create Path objects
folder_path = Path(folder_path_str)
file_path = folder_path / file_name 
# Use the '/' operator to join paths!

# Check if the file exists
if file_path.exists():
    print(f"The file '{file_name}' exists in '{folder_path}' and the new content hss been appended.")
    with open(todays_file, 'a') as m:
        m.write('\n' + '\n' + '---' + '\n' + content)
else:
    print(f"The file '{file_name}' does not exist in '{folder_path}'.")
    with open(todays_file, 'w') as m:
        m.write('---' +  '\n' + 'date: ' + todays_date + '\n' + 'title: ' + title_date + '\n' + '\n' + '---' + '\n' + '\n' +content)       


with open('hugoDraft.md', 'w', ) as f:
        print(f)