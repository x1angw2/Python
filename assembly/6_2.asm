; 利用栈 将定义的数据 逆序存放
assume cs:code

code segment
			dw 0123h, 0456h, 0789h, 0abch, 0defh, 0fedh, 0cbah, 0987h
			dw 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0					; 需要预先申请空间，直接使用默认的 SS:SP 貌似不行

	start:	mov ax,cs				; 
			mov ss,ax				; 定义栈地址，因为申请的空间在程序内，所以把 ss 指向系统分配的 cs
			mov sp,30h				; 两个 dw ，第一个共16个字节，第二个共 32 个字节，一共 10h + 10h x 2 = 30h  设置栈顶为 30h 

			mov cx,8
			mov bx,0
	s:		push cs:[bx]
			add bx,2
			loop s


			mov bx,0
			mov cx,8
	s0:		pop cs:[bx]
			add bx,2
			loop s0

			mov ax,4c00h
			int 21h
code ends

end start

