;; 计算 123 x 236
assume cs:code
code segment

	mov ax,236

	mov cx,122
s:	add ax,ax
	loop s

	mov ax,4c00h
	int 21h

code ends
end
