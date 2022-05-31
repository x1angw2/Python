assume cs:code,ds:data,ss:stack

data segment
	db 'abcdefghijklmnop'
data ends

stack segment
	db 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
stack ends

code segment

	start:	mov ax,data
			mov ds,ax

			mov ax,stack
			mov ss,ax

			mov ax,0

			mov ax,[bp]
			mov bx,[bx]

			mov cx,ss:[bx+bp]
			mov dx,ds:[bp]

			mov ax,4c00h
			int 21h

code ends

end start
