#/usr/bin/env python

import markdown2, os, sys, shutil, argparse
from bs4 import BeautifulSoup

#Find the first heading of some html. 
def find_title(html, alt=''):
	parsed = BeautifulSoup(html)
	i = 1
	while(i<7):
		h = parsed.findAll("h"+str(i))
		if(len(h) > 0):
			return h[0].get_text()
		i=i+1
	return alt
# Render a bunch of code. 
def md_render(code):
	return markdown2.markdown(code, extras=["footnotes", "fenced-code-blocks", "code-friendly"])

# Trys to read a file
def try_read(name):
	try:
		f = open(name)
		in_code = f.read()
		f.close()
	except IOError as e:
		print "[!] FATAL (READ): I/O error({0}): {1}".format(e.errno, e.strerror)
		sys.exit(1)
	except:
		print "[!] FATAL (READ): Unexpected error:", sys.exc_info()[0]
		sys.exit(1)
	return in_code

#Trys to write a file. 
def try_write(output_file, code):
	try:
		directory = os.path.dirname("./"+output_file)

		if not os.path.exists(directory):
			os.makedirs(directory)

		f=open(output_file, 'w+')
		f.write(code)
		f.close()
	except IOError as e:
		print "[!] FATAL (WRITE): I/O error({0}): {1}".format(e.errno, e.strerror)
		sys.exit(1)
	except:
		print "[!] FATAL (WRITE): Unexpected error:", sys.exc_info()[0]
		sys.exit(1)

#Creates the output surrounding the actual rendering. 
def output(render, title, body_only = False, css = True, header = "", prefix = "", suffix = ""):
	output = ""
	if not body_only:
		output += """<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>"""
		output += title
		output +="""</title>"""
		if css:
			output+= """
		<style type="text/css">
"""+get_css()+"""
		</style>"""

		output += header
		output += """
	</head>
	<body>
"""

	output += prefix+"\n"
	output += render
	output += suffix+"\n"

	if not body_only:
		output += """
	</body>
</html>"""

	return output

#Parse a text either a file or a text. 
def text_or_file(text):
	if text == "":
		return text
	if os.path.isfile(text):
		return try_read(text)
	return text


# Main Function running the logic
def main_run(infile, outfile, title, body, css, header, prefix, suffix):
	header = text_or_file(header)
	prefix = text_or_file(prefix)
	suffix = text_or_file(suffix)
	render = md_render(try_read(infile))
	if title == "":
		title = find_title(render)
	
	res = output(render, title, body, css, header, prefix, suffix)
	if outfile == "":
		print res
	else:
		
		try_write(outfile, res)

# Main Arg parsing function
def main(cargs):
	parser = argparse.ArgumentParser(description='Python Markdown Compiler')
	parser.add_argument('INPUT_FILE', nargs=1, help='Input file. ')
	parser.add_argument('-o', nargs=1, default=[""], help="Output File. Defaults to STDOUT. ", metavar="OUTPUT_FILE", dest="OUTPUT_FILE")
	parser.add_argument('--title', '-t', dest="TITLE", nargs=1, default=[""], metavar="TITLE", help="Use a custom html title. ")
	parser.add_argument('--no-css','-u', action='store_const', const=False, default=True, dest="MAKE_CSS", help="Do not include stylesheet. ")
	parser.add_argument('--body-only', '-b', action='store_const', const=True, default=False, dest="BODY_ONLY", help="Generate HTML body only. ")
	parser.add_argument('--header', '-he', nargs=1, dest="HEADER", metavar="HEADER", help="Include a file or a string in the header. ", default=[""])

	parser.add_argument('--body-prefix', '-pre', nargs=1, dest="BODY_PREFIX", metavar="BODY_PREFIX", help="Include a file or a string before the content in the body. ", default=[""])
	parser.add_argument('--body-suffix','-suf',  nargs=1, dest="BODY_SUFFIX", metavar="BODY_SUFFIX", help="Include a file or a string after the content in the body. ", default=[""])

	args = parser.parse_args()

	if(os.path.isfile(args.INPUT_FILE[0])):
		main_run(args.INPUT_FILE[0], args.OUTPUT_FILE[0], args.TITLE[0], args.BODY_ONLY, args.MAKE_CSS, args.HEADER[0], args.BODY_PREFIX[0], args.BODY_SUFFIX[0])
	else:
		print "[!] INPUT_FILE is not a file. "
		
			
#CSS code stuff
def get_css():
	css_code = """/* Basic styles https://gist.github.com/cpatuzzo/3331384 */
		body {
		  font-family: Helvetica, arial, sans-serif;
		  font-size: 14px;
		  line-height: 1.6;
		  padding-top: 10px;
		  padding-bottom: 10px;
		  background-color: white;
		  padding: 30px;
		  color: #333;
		}
		 
		body > *:first-child {
		  margin-top: 0 !important;
		}
		 
		body > *:last-child {
		  margin-bottom: 0 !important;
		}
		 
		a {
		  color: #4183C4;
		  text-decoration: none;
		}
		 
		a.absent {
		  color: #cc0000;
		}
		 
		a.anchor {
		  display: block;
		  padding-left: 30px;
		  margin-left: -30px;
		  cursor: pointer;
		  position: absolute;
		  top: 0;
		  left: 0;
		  bottom: 0;
		}
		 
		h1, h2, h3, h4, h5, h6 {
		  margin: 20px 0 10px;
		  padding: 0;
		  font-weight: bold;
		  -webkit-font-smoothing: antialiased;
		  cursor: text;
		  position: relative;
		}
		 
		h2:first-child, h1:first-child, h1:first-child + h2, h3:first-child, h4:first-child, h5:first-child, h6:first-child {
		  margin-top: 0;
		  padding-top: 0;
		}
		 
		h1:hover a.anchor, h2:hover a.anchor, h3:hover a.anchor, h4:hover a.anchor, h5:hover a.anchor, h6:hover a.anchor {
		  text-decoration: none;
		}
		 
		h1 tt, h1 code {
		  font-size: inherit;
		}
		 
		h2 tt, h2 code {
		  font-size: inherit;
		}
		 
		h3 tt, h3 code {
		  font-size: inherit;
		}
		 
		h4 tt, h4 code {
		  font-size: inherit;
		}
		 
		h5 tt, h5 code {
		  font-size: inherit;
		}
		 
		h6 tt, h6 code {
		  font-size: inherit;
		}
		 
		h1 {
		  font-size: 28px;
		  color: black;
		}
		 
		h2 {
		  font-size: 24px;
		  border-bottom: 1px solid #cccccc;
		  color: black;
		}
		 
		h3 {
		  font-size: 18px;
		}
		 
		h4 {
		  font-size: 16px;
		}
		 
		h5 {
		  font-size: 14px;
		}
		 
		h6 {
		  color: #777777;
		  font-size: 14px;
		}
		 
		p, blockquote, ul, ol, dl, table, pre {
		  margin: 15px 0;
		}

		li {
		  margin: 7px 0;		
		}
		 
		hr {
		  border: 0 none;
		  color: #cccccc;
		  height: 4px;
		  padding: 0;
		}
		 
		body > h2:first-child {
		  margin-top: 0;
		  padding-top: 0;
		}
		 
		body > h1:first-child {
		  margin-top: 0;
		  padding-top: 0;
		}
		 
		body > h1:first-child + h2 {
		  margin-top: 0;
		  padding-top: 0;
		}
		 
		body > h3:first-child, body > h4:first-child, body > h5:first-child, body > h6:first-child {
		  margin-top: 0;
		  padding-top: 0;
		}
		 
		a:first-child h1, a:first-child h2, a:first-child h3, a:first-child h4, a:first-child h5, a:first-child h6 {
		  margin-top: 0;
		  padding-top: 0;
		}
		 
		h1 p, h2 p, h3 p, h4 p, h5 p, h6 p {
		  margin-top: 0;
		}
		 
		li p.first {
		  display: inline-block;
		}
		 
		ul, ol {
		  padding-left: 30px;
		}
		 
		ul :first-child, ol :first-child {
		  margin-top: 0;
		}
		 
		ul :last-child, ol :last-child {
		  margin-bottom: 0;
		}
		 
		dl {
		  padding: 0;
		}
		 
		dl dt {
		  font-size: 14px;
		  font-weight: bold;
		  font-style: italic;
		  padding: 0;
		  margin: 15px 0 5px;
		}
		 
		dl dt:first-child {
		  padding: 0;
		}
		 
		dl dt > :first-child {
		  margin-top: 0;
		}
		 
		dl dt > :last-child {
		  margin-bottom: 0;
		}
		 
		dl dd {
		  margin: 0 0 15px;
		  padding: 0 15px;
		}
		 
		dl dd > :first-child {
		  margin-top: 0;
		}
		 
		dl dd > :last-child {
		  margin-bottom: 0;
		}
		 
		blockquote {
		  border-left: 4px solid #dddddd;
		  padding: 0 15px;
		  color: #777777;
		}
		 
		blockquote > :first-child {
		  margin-top: 0;
		}
		 
		blockquote > :last-child {
		  margin-bottom: 0;
		}
		 
		table {
		  padding: 0;
		}
		table tr {
		  border-top: 1px solid #cccccc;
		  background-color: white;
		  margin: 0;
		  padding: 0;
		}
		 
		table tr:nth-child(2n) {
		  background-color: #f8f8f8;
		}
		 
		table tr th {
		  font-weight: bold;
		  border: 1px solid #cccccc;
		  text-align: left;
		  margin: 0;
		  padding: 6px 13px;
		}
		 
		table tr td {
		  border: 1px solid #cccccc;
		  text-align: left;
		  margin: 0;
		  padding: 6px 13px;
		}
		 
		table tr th :first-child, table tr td :first-child {
		  margin-top: 0;
		}
		 
		table tr th :last-child, table tr td :last-child {
		  margin-bottom: 0;
		}
		 
		img {
		  max-width: 100%;
		}
		 
		span.frame {
		  display: block;
		  overflow: hidden;
		}
		 
		span.frame > span {
		  border: 1px solid #dddddd;
		  display: block;
		  float: left;
		  overflow: hidden;
		  margin: 13px 0 0;
		  padding: 7px;
		  width: auto;
		}
		 
		span.frame span img {
		  display: block;
		  float: left;
		}
		 
		span.frame span span {
		  clear: both;
		  color: #333333;
		  display: block;
		  padding: 5px 0 0;
		}
		 
		span.align-center {
		  display: block;
		  overflow: hidden;
		  clear: both;
		}
		 
		span.align-center > span {
		  display: block;
		  overflow: hidden;
		  margin: 13px auto 0;
		  text-align: center;
		}
		 
		span.align-center span img {
		  margin: 0 auto;
		  text-align: center;
		}
		 
		span.align-right {
		  display: block;
		  overflow: hidden;
		  clear: both;
		}
		 
		span.align-right > span {
		  display: block;
		  overflow: hidden;
		  margin: 13px 0 0;
		  text-align: right;
		}
		 
		span.align-right span img {
		  margin: 0;
		  text-align: right;
		}
		 
		span.float-left {
		  display: block;
		  margin-right: 13px;
		  overflow: hidden;
		  float: left;
		}
		 
		span.float-left span {
		  margin: 13px 0 0;
		}
		 
		span.float-right {
		  display: block;
		  margin-left: 13px;
		  overflow: hidden;
		  float: right;
		}
		 
		span.float-right > span {
		  display: block;
		  overflow: hidden;
		  margin: 13px auto 0;
		  text-align: right;
		}
		 
		code, tt {
		  margin: 0 2px;
		  padding: 0 5px;
		  white-space: nowrap;
		  border: 1px solid #eaeaea;
		  background-color: #f8f8f8;
		  border-radius: 3px;
		}
		 
		pre code {
		  margin: 0;
		  padding: 0;
		  white-space: pre;
		  border: none;
		  background: transparent;
		}
		 
		.highlight pre {
		  background-color: #f8f8f8;
		  border: 1px solid #cccccc;
		  font-size: 13px;
		  line-height: 19px;
		  overflow: auto;
		  padding: 6px 10px;
		  border-radius: 3px;
		}
		 
		pre {
		  background-color: #f8f8f8;
		  border: 1px solid #cccccc;
		  font-size: 13px;
		  line-height: 19px;
		  overflow: auto;
		  padding: 6px 10px;
		  border-radius: 3px;
		}
		 
		pre code, pre tt {
		  background-color: transparent;
		  border: none;
		}
		
		/* Syntax Highlights */
		.hll { background-color: #ffffcc }
		.c { color: #999988; font-style: italic } /* Comment */
		.err { color: #a61717; background-color: #e3d2d2 } /* Error */
		.k { color: #000000; font-weight: bold } /* Keyword */
		.o { color: #000000; font-weight: bold } /* Operator */
		.cm { color: #999988; font-style: italic } /* Comment.Multiline */
		.cp { color: #999999; font-weight: bold; font-style: italic } /* Comment.Preproc */
		.c1 { color: #999988; font-style: italic } /* Comment.Single */
		.cs { color: #999999; font-weight: bold; font-style: italic } /* Comment.Special */
		.gd { color: #000000; background-color: #ffdddd } /* Generic.Deleted */
		.ge { color: #000000; font-style: italic } /* Generic.Emph */
		.gr { color: #aa0000 } /* Generic.Error */
		.gh { color: #999999 } /* Generic.Heading */
		.gi { color: #000000; background-color: #ddffdd } /* Generic.Inserted */
		.go { color: #888888 } /* Generic.Output */
		.gp { color: #555555 } /* Generic.Prompt */
		.gs { font-weight: bold } /* Generic.Strong */
		.gu { color: #aaaaaa } /* Generic.Subheading */
		.gt { color: #aa0000 } /* Generic.Traceback */
		.kc { color: #000000; font-weight: bold } /* Keyword.Constant */
		.kd { color: #000000; font-weight: bold } /* Keyword.Declaration */
		.kn { color: #000000; font-weight: bold } /* Keyword.Namespace */
		.kp { color: #000000; font-weight: bold } /* Keyword.Pseudo */
		.kr { color: #000000; font-weight: bold } /* Keyword.Reserved */
		.kt { color: #445588; font-weight: bold } /* Keyword.Type */
		.m { color: #009999 } /* Literal.Number */
		.s { color: #d01040 } /* Literal.String */
		.na { color: #008080 } /* Name.Attribute */
		.nb { color: #0086B3 } /* Name.Builtin */
		.nc { color: #445588; font-weight: bold } /* Name.Class */
		.no { color: #008080 } /* Name.Constant */
		.nd { color: #3c5d5d; font-weight: bold } /* Name.Decorator */
		.ni { color: #800080 } /* Name.Entity */
		.ne { color: #990000; font-weight: bold } /* Name.Exception */
		.nf { color: #990000; font-weight: bold } /* Name.Function */
		.nl { color: #990000; font-weight: bold } /* Name.Label */
		.nn { color: #555555 } /* Name.Namespace */
		.nt { color: #000080 } /* Name.Tag */
		.nv { color: #008080 } /* Name.Variable */
		.ow { color: #000000; font-weight: bold } /* Operator.Word */
		.w { color: #bbbbbb } /* Text.Whitespace */
		.mf { color: #009999 } /* Literal.Number.Float */
		.mh { color: #009999 } /* Literal.Number.Hex */
		.mi { color: #009999 } /* Literal.Number.Integer */
		.mo { color: #009999 } /* Literal.Number.Oct */
		.sb { color: #d01040 } /* Literal.String.Backtick */
		.sc { color: #d01040 } /* Literal.String.Char */
		.sd { color: #d01040 } /* Literal.String.Doc */
		.s2 { color: #d01040 } /* Literal.String.Double */
		.se { color: #d01040 } /* Literal.String.Escape */
		.sh { color: #d01040 } /* Literal.String.Heredoc */
		.si { color: #d01040 } /* Literal.String.Interpol */
		.sx { color: #d01040 } /* Literal.String.Other */
		.sr { color: #009926 } /* Literal.String.Regex */
		.s1 { color: #d01040 } /* Literal.String.Single */
		.ss { color: #990073 } /* Literal.String.Symbol */
		.bp { color: #999999 } /* Name.Builtin.Pseudo */
		.vc { color: #008080 } /* Name.Variable.Class */
		.vg { color: #008080 } /* Name.Variable.Global */
		.vi { color: #008080 } /* Name.Variable.Instance */
		.il { color: #009999 } /* Literal.Number.Integer.Long */"""
	return css_code

if __name__ == "__main__":
	main(sys.argv)
