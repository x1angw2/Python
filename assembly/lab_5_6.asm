; 用 push 指令将 a 段中的前 8 个字形数据，逆序复制到 b 段中
assume cs:code,ds:a

a segment
	dw 1, 2, 3, 4, 5, 6, 7, 8, 9, 0ah, 0bh, 0ch, 0dh, 0eh, 0fh, 0ffh
a ends

b segment
	dw 0, 0, 0, 0, 0, 0, 0, 0
b ends

; 将 b 段定义为栈即可

code segment

	start:	mov ax, a
			add ax, 2			; a 段一共 16 个字形数据，偏移量为 2
			mov ss, ax
			mov sp, 10h			; 定义栈

			mov ax, a
			mov ds, ax			; 定义 data 段

			mov cx, 8
			mov bx, 0			; 定义 循环次数 cx 和 变量 bx
		s:	push [bx]
			add bx, 2			; 字型数据 偏移量为 2
			loop s

			mov ax, 4c00h
			int 21h


code ends

end start

