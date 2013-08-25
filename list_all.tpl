<p>The open items are as follows:</p>
<table border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
    <href>
  %end
  <script language="javascript" type="text/javascript">
  	var number = "http://localhost:8215/edit/" + row[0]
  </script>
  <form>
  	<a href="" onClick="location.href=this.href +'?key=' +number;return false";>Editing</a> 
  </form>
  </tr>
%end
</table>