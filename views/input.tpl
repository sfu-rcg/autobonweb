<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>autobonweb</title>
    </head>
  <body>
    <div id="app">

      <h3>quick and dirty bon_csv2html front end</h3>
      <h2>
	[<a href="http://{{ bind_addr }}/{{ results_url_root }}">results</a>]
      </h2>

      <form action="/ingest" method="POST">

	<table border="0" cellspacing="4" cellpadding="4">
	  <tr>
	    <td align="right"><b>Date</b></td>
	    <td><input type="text" name="date" value="{{ date }}" /></td>
	  </tr>
	  <tr>
	    <td align="right"><b>Load Source</b> (host or lab)</b></td>
	    <td><input type="text" name="load_gen" /></td>
	  </tr>
	  <tr>
	    <td align="right"><b>Target NFS Server</b></td>
	    <td><input type="text" name="target" /></td>
	  </tr>
	  <tr>
	    <td align="right"><b>Filesystem Type</b></td>
	    <td>
	      <select name="fs_type">
		<option value="xfs">XFS</option>
		<option value="zfs">ZFS</option>
	      </select>
	    </td>
	  </tr>
	  <tr>
	    <td align="right"><b>NFS Security Level</b></td>
	    <td>
	      <select name="sec_level">
		<option value="sys">sys</option>
		<option value="krb5i">krb5i</option>
		<option value="krb5p">krb5p</option>
	      </select>
	    </td>
	  </tr>
	  <tr>
	    <td align="right"><b>Tag</b> (no spaces)</td>
	    <td><input type="text" name="tag" /></td>
	  </tr>

	  <tr>
	    <td align="right"><b>Write to disk</td>
	    <td><input type="checkbox" name="write_to_disk" value="1" checked /></td>
	  </tr>


	</table>
	<p>
	  Paste your unfiltered bonnie++ 1.97 syslog output here: <br />
	  <textarea rows="10" cols="80" name="meat"></textarea>
	</p>
<input type="submit" name="energize" value="energize" />

      </form>

    </div>
  </body>
</html>
