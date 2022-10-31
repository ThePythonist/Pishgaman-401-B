people = [
    {"Name":"Nima","Age":16,"Job":"Front-End"},
    {"Name":"Amin","Age":16,"Job":"Back-End"},
    {"Name":"Kiarash","Age":18,"Job":"Back-End"},
    {"Name":"Meisam","Age":18,"Job":"DB-Man"},
    {"Name":"Sepideh","Age":13,"Job":"Back-End"}
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #aa0454;
  color: white;
}
</style>
</head>
<body>

<h1>Table of employees</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Age</th>
    <th>Job</th>
  </tr>
"""

for person in people:
    html += f"""
  <tr>
    <td>{person["Name"]}</td>
    <td>{person["Age"]}</td>
    <td>{person["Job"]}</td>
  </tr>
    """

html += """
</table>
</body>
</html>
"""

open("Template.html","w").write(html)
print("Done")
