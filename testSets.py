
csv = set()
shp = set()

for value in range(1, 10):
    csv.add(value)

for value in range(9, 12):
    shp.add(value)



print 'csv---' ,csv
print 'shp---' ,shp

not_in_csv = set.difference(shp, csv)
not_in_shp = set.difference(csv, shp)

print "not_in_csv", len(not_in_csv), not_in_csv
print "not_in_shp", len(not_in_shp), not_in_shp


#adding comment 1 . for testing upload on git


