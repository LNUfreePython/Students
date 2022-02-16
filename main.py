import log_con

def variant_7(a,b,c):
	res=log_con.lnot(b)
	res=log_con.lor(a,res)
	left=log_con.land(res,c)
	res=log_con.lnot(b)
	right=log_con.lor(res,c)
	return log_con.lequ(left,right)

variant_7(True,True,True)
variant_7(False,False,False)
variant_7(True,True,False)
variant_7(True,False,False)
variant_7(False,True,False)
variant_7(False,True,True)

print("1")








		



