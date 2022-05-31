; 功能	不溢出除法
; 参数	ax = dword 的低 16 位	dx = dword 的高 16 位
;		cx = 除数
; 返回	dx = 商的高 16 位   ax = 商的低 16 位
;		cx = 余数
assume cs:codesg

codesg segment

	start:	mov ax, 4220h
			mov dx, 000fh
			mov cx, 0ah

			call divdw

			mov ax, 4c00h
			int 21h



	divdw:	push bx

			push ax							; 先保存 被除数低四位
			mov ax, dx					
			mov dx, 0
			div cx							; 把高四位设为低四位来除
											; 商在 ax 中  余数在 dx 中
			mov bx,ax						; 注意 push  bx  把高位商保存   保存商
											; dx 为余数 需要和 原来的低四位相加  可以不用动
			pop ax							; 取出 低四位

			div cx							; 直接除   dx 为余数  ax 为商

			mov cx, dx						; 把余数移动 cx
			mov dx, bx						; 取高位商 保存到 dx

			pop bx
			ret


			

codesg ends

end start

