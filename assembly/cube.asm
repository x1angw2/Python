; 说明：计算 N 的 3 次方
; 参数：(bx) = N
; 结果：(dx:ax) = N^3

cube:	mov ax,bx
		mul bx
		mul bx
		ret
