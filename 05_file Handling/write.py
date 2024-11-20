print("----------------------------------Write to file----------------------------------------")
# First round:
# Open a file in write mode
f = open("D:/test.txt", "w", encoding="UTF-8")
# write content
f.write("Hello World!!!")  # Content is written to the memory buffer
# flush content
f.flush()  # Flush the content from memory to the file on disk
# close file
f.close()  # The close method includes the functionality of flush, so the previous flush is optional


# Second round:
# Open a file in write mode
f = open("D:/test.txt", "w", encoding="UTF-8")
# write content & flush
f.write("Have a nice day!!!")
# close file
f.close()
# In "w" mode, existing file content is overwritten by the new content, so the final content of the file is
# Have a nice day!!!


print("----------------------------------Append to file----------------------------------------")
# Open a file in append mode, by setting "a" as the mode
f = open("D:/test.txt", "a", encoding="UTF-8")
# write content & flush
f.write("\nSee you tomorrow!!!")
# close file
f.close()
# Now, the final content of the file is:
# Have a nice day!!!
# See you tomorrow!!!

