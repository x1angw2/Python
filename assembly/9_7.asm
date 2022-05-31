
; jcxz		jump [cx]register zero
; 如果 cx == 0 则跳转  
; 和 loop 相逆


; 利用 jcxz 指令，实现在内存 2000h 段中查找第一个值为 0 的字节

assume cs:codesg

codesg segment

	start:	mov ax, 2000h
			mov ds, ax
			mov bx, 0

		; s:	___
		;		___
		;		___
		;		___

		s:	mov cx,0
			mov cl, ds:[bx]
			jcxz ok
			inc bx

			jmp short s

		ok: mov dx,bx
			
			mov ax,4c00h
			int 21h

codesg ends

end start

