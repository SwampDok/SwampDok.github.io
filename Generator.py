# -*- coding: utf-8 -*-
import sqlite3

f = open('table.html', 'w')

conn = sqlite3.connect('Projects.db')
c = conn.cursor()
d = conn.cursor()

sections = []

d.execute('SELECT * FROM Section ')
row = d.fetchone()
while row is not None:
    sections.append(str(row[1]))
    row = d.fetchone()

f.writelines('<table>')

for i in range(0, len(sections)):
    
    c.execute('SELECT * FROM Projects WHERE Section = ' + str(i+1))
    
    f.writelines('''<tr class = 'Title'>
			<td colspan="2">
				<h2> %s </h2> 
			</td>
		</tr>''' % sections[i])
    row = c.fetchone()
    while row is not None:
        f.writelines('''<tr class = 'Content'>
                            <td width = '20%'>
                                {0}
                            </td>
                            <td width = '80%'>
                                {1}
                            </td>
                        </tr>'''.format(str(row[0]) + '# ' + str(row[1]), str(row[2])))
        row = c.fetchone()

f.writelines('</table>')


# закрываем соединение с базой
c.close()
d.close()
conn.close()
f.close ()