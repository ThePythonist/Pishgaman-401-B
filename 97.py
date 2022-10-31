entry = input("Entry : ")
entry2 = input("Entry : ")
# output = "<p>{}</p>".format(entry)
output = f"""
<h1>{entry}</h1>
<p>{entry2}</p>
"""
open("Test.html","w").write(output)
print("Done")
