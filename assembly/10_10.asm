assume cs:codesg

data segment
	dw 1, 2, 3, 4, 5, 6, 7, 8
	dd 0, 0, 0, 0, 0, 0, 0, 0
data ends

codesg segment

	start:	mov ax, data
			mov ds, ax
			mov si, 0				; ds:si 指向第一组 word 单元
			mov di, 16				; ds:si 指向第二组 dword 单元

			mov cx, 8
		s:	mov bx, [si]
			call cube
			mov [di], ax
			mov [di].2, dx
			add si, 2				; ds:si 指向下一个 word 单元
			add di, 4				; ds:si 指向下一个 dword 单元
			loop s

			mov ax, 4c00h
			int 21h


	cube:	mov ax, bx
			mul bx
			mul bx
			ret

codesg ends

end start

