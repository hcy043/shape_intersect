points = []
epsilon=0.001
def is_equal(fp1,fp2):
	return abs(fp1-fp2) < epsilon
def area_of_triangle(triangle):#[(x1,y1),(x2,y2),(x3,y3)]
	p1,p2,p3 = triangle
	x1,y1 = p1
	x2,y2 = p2
	x3,y3 = p3
	#print x1,y1,x2,y2,x3,y3
	area_of_triangle = (1/2.)*abs(float(x1)*y2+x2*y3+x3*y1-(y1*x2+y2*x3+y3*x1))
	return area_of_triangle
def points_in_triangle(triangle, other_shape):
	global points
	total_area = area_of_triangle(triangle)
	p1,p2,p3 = triangle
	valid_points = []
	for i in other_shape:
		sum_of_triangle_pieces = area_of_triangle([p1,p2,i]) + area_of_triangle([p1,p3,i]) + area_of_triangle([p2,p3,i])
	  # print sum_of_triangle_pieces, total_area,i
		if abs(sum_of_triangle_pieces-total_area)<epsilon:
			if i not in points: valid_points.append(i)
	return valid_points#returns a list
def line_intersect(line1, line2):#[(x1,y1),(x2,y2)],[(x3,y3),(x4,y3)]
	global points
	x1,y1=line1[0]
	x2,y2=line1[1]
	x3,y3=line2[0]
	x4,y4=line2[1]
	a1 = float(y2) - y1#I spent 4-5 hours on this function. And making an operand float was the solution :(
	a2 = y4 - y3
	b1 = x1 - x2
	b2 = x3 - x4
	c1 = a1*x1 + b1*y1
	c2 = a2*x3 + b2*y3
	det= a1*b2 - a2*b1 #determinant of the two equations
	if det != 0 and det != 0.0:#TEST IT FOR PARALEL LINES!!!!!!!!!!!!1@@@@@@@@@@@@@@@@@@@@@@@
		x = (c1*b2-b1*c2)/det #crimer's rule
		y = (a1*c2 - a2*c1)/det #crimer's rule
		x,y = x+0,y+0 #to avoid -0 
		# min(x1,x2) <= x <= max(x1,x2)
		# min(x3,x4) <= x <= max(x3,x4)
		# min(y1,y2) <= y <= max(y1,y2)
		# min(y3,y4) <= y <= max(y3,y4)
		if (min(x1,x2) < x or is_equal(min(x1,x2),x)) and (x < max(x1,x2) or is_equal(max(x1,x2),x)) and (min(x3,x4) < x or is_equal(min(x3,x4),x)) and (x < max(x3,x4) or is_equal(max(x3,x4),x)) and (min(y1,y2) < y or is_equal(min(y1,y2),y)) and (y < max(y1,y2) or is_equal(max(y1,y2),y)) and  (min(y3,y4) < y or is_equal(min(y3,y4),y)) and (y < max(y3,y4) or is_equal(min(y3,y4),y)):
			##print points, (x+0,y+0) not in points, (x+0,y+0)
			if (x,y) not in points: return (x,y)#(x,y)
	return None		  
def points_in_rectangle(rectangle,other_shape):
	#first decide if its concave or not and find the irregular point
	p1,p2,p3,p4 = rectangle
	valid_points = []
	#determine if its concave or convex
	#if diagonals intersect, then its convex
	if line_intersect([p1,p3],[p2,p4]) == None: #concave
		#lets find the biggest area, which irregular point not in
		area1,area2,area3,area4 = 0,0,0,0
		area1 = area_of_triangle([p1,p3,p2])
		area2 = area_of_triangle([p1,p3,p4])
		area3 = area_of_triangle([p2,p4,p1])
		area4 = area_of_triangle([p2,p4,p3])
		biggest_area=max(area1,area2,area3,area4)
		irregular_point= 0 #
		cool_point=0 #
		other_points=[]
		if is_equal(area1,biggest_area): 
			irregular_point=p4
			cool_point=p2
			other_points.extend([p1,p3])
		elif is_equal(area2,biggest_area): 
			irregular_point=p2
			cool_point=p4
			other_points.extend([p1,p3])
		elif is_equal(area3,biggest_area): 
			irregular_point=p3
			cool_point=p1
			other_points.extend([p2,p4])
		elif is_equal(area4,biggest_area): 
			irregular_point=p1
			cool_point=p3
			other_points.extend([p2,p4])
		#find the fucking point :D
		for i in other_shape:
			if len(points_in_triangle([cool_point,irregular_point,other_points[0]],[i]))>0 or len(points_in_triangle([cool_point,irregular_point,other_points[1]],[i]))>0:
				valid_points.append(i)# this was points.append 
	else:#convex
		area_of_rectangle = area_of_triangle([p1,p2,p3]) + area_of_triangle([p1,p3,p4])
		for i in other_shape:
			new_area = area_of_triangle([p1,p2,i])
			new_area += area_of_triangle([p2,p3,i])
			new_area += area_of_triangle([p3,p4,i])
			new_area += area_of_triangle([p4,p1,i])
			if is_equal(new_area, area_of_rectangle): valid_points.append(i)
	return valid_points
def minority_shape_intersect(shape1, shape2):
	global points
	points = []
	#print len(shape1), len(shape2)
	if len(shape1) == 3 and len(shape2) == 3: #both triangle
		s1p1,s1p2,s1p3 = shape1#shape1's points
		s2p1,s2p2,s2p3 = shape2#shape2's points
		
		#shape1 line of point 1 and point 2 vs all lines of shape2
		if line_intersect([s1p1,s1p2],[s2p1,s2p2]) != None: points.append(line_intersect([s1p1,s1p2],[s2p1,s2p2])) 
		if line_intersect([s1p1,s1p2],[s2p2,s2p3]) != None: points.append(line_intersect([s1p1,s1p2],[s2p2,s2p3]))
		if line_intersect([s1p1,s1p2],[s2p3,s2p1]) != None: points.append(line_intersect([s1p1,s1p2],[s2p3,s2p1]))
	   
		if line_intersect([s1p2,s1p3],[s2p1,s2p2]) != None: points.append(line_intersect([s1p2,s1p3],[s2p1,s2p2]))
		if line_intersect([s1p2,s1p3],[s2p2,s2p3]) != None: points.append(line_intersect([s1p2,s1p3],[s2p2,s2p3]))
		if line_intersect([s1p2,s1p3],[s2p3,s2p1]) != None: points.append(line_intersect([s1p2,s1p3],[s2p3,s2p1]))
		
		if line_intersect([s1p3,s1p1],[s2p1,s2p2]) != None: points.append(line_intersect([s1p3,s1p1],[s2p1,s2p2]))
		if line_intersect([s1p3,s1p1],[s2p2,s2p3]) != None: points.append(line_intersect([s1p3,s1p1],[s2p2,s2p3]))
		if line_intersect([s1p3,s1p1],[s2p3,s2p1]) != None: points.append(line_intersect([s1p3,s1p1],[s2p3,s2p1]))
		#points in each area check:
		if len(points_in_triangle(shape1,shape2)) >0: 
			for i in points_in_triangle(shape1,shape2):
				if i not in points: points.append(i)
		if len(points_in_triangle(shape2,shape1)) >0:
			for i in points_in_triangle(shape2,shape1):
				if i not in points: points.append(i)

	elif (len(shape1) == 4 and len(shape2) ==3) or (len(shape1)== 3 and len(shape2)==4):#rectangle vs triangle
		rectangle = shape1 if len(shape1)==4 else shape2
		triangle = shape2 if len(shape2)==3 else shape1
		#first find line intersections.
		#r1,r2,r3,r4 vs t1,t2,t3 rect. vs triangle
		r1,r2,r3,r4 = rectangle
		t1,t2,t3 = triangle

		#t1-t2 line
		if line_intersect([t1,t2],[r1,r2]) != None: points.append(line_intersect([t1,t2],[r1,r2])) 
		if line_intersect([t1,t2],[r2,r3]) != None: points.append(line_intersect([t1,t2],[r2,r3]))
		if line_intersect([t1,t2],[r3,r4]) != None: points.append(line_intersect([t1,t2],[r3,r4]))
		if line_intersect([t1,t2],[r4,r1]) != None: points.append(line_intersect([t1,t2],[r4,r1]))

		#print line_intersect([t1,t2],[r1,r2])
		#t2-t3 line
		if line_intersect([t2,t3],[r1,r2]) != None: points.append(line_intersect([t2,t3],[r1,r2])) 
		if line_intersect([t2,t3],[r2,r3]) != None: points.append(line_intersect([t2,t3],[r2,r3]))
		if line_intersect([t2,t3],[r3,r4]) != None: points.append(line_intersect([t2,t3],[r3,r4]))
		if line_intersect([t2,t3],[r4,r1]) != None: points.append(line_intersect([t2,t3],[r4,r1]))
		
		#t3-t1 line
		if line_intersect([t3,t1],[r1,r2]) != None: points.append(line_intersect([t3,t1],[r1,r2])) 
		if line_intersect([t3,t1],[r2,r3]) != None: points.append(line_intersect([t3,t1],[r2,r3]))
		if line_intersect([t3,t1],[r3,r4]) != None: points.append(line_intersect([t3,t1],[r3,r4]))
		if line_intersect([t3,t1],[r4,r1]) != None: points.append(line_intersect([t3,t1],[r4,r1]))

		#points in triangle
		if len(points_in_triangle(triangle,rectangle)) >0:
			for i in points_in_triangle(triangle,rectangle):
				if i not in points: points.append(i)
		#points in rectangle
		if len(points_in_rectangle(rectangle,triangle)) >0: 
			for i in points_in_rectangle(rectangle, triangle):
				if i not in points: points.append(i)
	elif len(shape1)==4 and len(shape2)==4:
		r1,r2,r3,r4 = shape1#first rectangle
		q1,q2,q3,q4 = shape2#second rectangle
		#first line check
		#r1,r2 line
		if line_intersect([r1,r2],[q1,q2]) != None: points.append(line_intersect([r1,r2],[q1,q2])) 
		if line_intersect([r1,r2],[q2,q3]) != None: points.append(line_intersect([r1,r2],[q2,q3]))
		if line_intersect([r1,r2],[q3,q4]) != None: points.append(line_intersect([r1,r2],[q3,q4]))
		if line_intersect([r1,r2],[q4,q1]) != None: points.append(line_intersect([r1,r2],[q4,q1]))
		
		#r2,r3 line
		if line_intersect([r2,r3],[q1,q2]) != None: points.append(line_intersect([r2,r3],[q1,q2])) 
		if line_intersect([r2,r3],[q2,q3]) != None: points.append(line_intersect([r2,r3],[q2,q3]))
		if line_intersect([r2,r3],[q3,q4]) != None: points.append(line_intersect([r2,r3],[q3,q4]))
		if line_intersect([r2,r3],[q4,q1]) != None: points.append(line_intersect([r2,r3],[q4,q1]))
		
		#r3,r4 line
		if line_intersect([r3,r4],[q1,q2]) != None: points.append(line_intersect([r3,r4],[q1,q2])) 
		if line_intersect([r3,r4],[q2,q3]) != None: points.append(line_intersect([r3,r4],[q2,q3]))
		if line_intersect([r3,r4],[q3,q4]) != None: points.append(line_intersect([r3,r4],[q3,q4]))
		if line_intersect([r3,r4],[q4,q1]) != None: points.append(line_intersect([r3,r4],[q4,q1]))
		
		#r4,r1 line
		if line_intersect([r4,r1],[q1,q2]) != None: points.append(line_intersect([r4,r1],[q1,q2])) 
		if line_intersect([r4,r1],[q2,q3]) != None: points.append(line_intersect([r4,r1],[q2,q3]))
		if line_intersect([r4,r1],[q3,q4]) != None: points.append(line_intersect([r4,r1],[q3,q4]))
		if line_intersect([r4,r1],[q4,q1]) != None: points.append(line_intersect([r4,r1],[q4,q1]))
#now, check points in each :)
		if len(points_in_rectangle(shape1,shape2)) >0:#if this point was not marked before. 
			for i in points_in_rectangle(shape1,shape2):
				if i not in points: points.append(i)
		if len(points_in_rectangle(shape2,shape1)) >0:
			for i in points_in_rectangle(shape2,shape1):
				if i not in points: points.append(i)
	return points if len(points) > 2 else []# return iff its a polygon