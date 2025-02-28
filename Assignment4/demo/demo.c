/* 

This is a decompilation from the original binary ais3_crackme

Online decompiler
https://dogbolt.org/?id=a27cad78-65c8-4191-8b6f-06b0803e5215#angr=107

*/

extern char encrypted;  // External reference to an encrypted string or array.

/* Each char in a0 is transformed and compared to encrypted */
int verify(char *a0)  // Function to verify input string 'a0'.
{
    char v0;  // Temporary variable for transformation.
    unsigned int v1;  // Loop index.

    // Loop through each character in the input string.
    for (v1 = 0; a0[v1]; v1 += 1)
    {
        v0 = v1 ^ a0[v1];  // XOR the index with the character in 'a0'.
        
        // Perform a bitwise rotation: right shift by (8 - ((v1 ^ 9) & 3)) & 31
        // and left shift by ((v1 ^ 9) & 3) & 31.
        v0 = v0 >> ((char)(8 - ((v1 ^ 9) & 3)) & 31) | v0 << ((char)((v1 ^ 9) & 3) & 31);
        
        v0 += 8;  // Add 8 to the transformed value.
        
        // Compare with the corresponding value in the 'encrypted' array.
        if (*(&(&encrypted)[v1]) != v0)
            return 0;  // Return 0 if any character does not match.
    }
    
    // Return true (1) only if the input length is exactly 23.
    return v1 == 23;
}

int main(unsigned int a0, struct_0 *a1)
{
    unsigned int v1;  // Temporary variable to store verification result

    if (a0 != 2)  // Check if the first argument (a0) is not 2
    {
        puts("You need to enter the secret key!");  // Print error message
        return -1;  // Return error value
    }

    v1 = verify(a1->field_8);  // Verify the secret key by calling the verify function
    if (v1)  // If verification is successful
        puts("Correct! that is the secret key!");  // Print success message
    else
        puts("I'm sorry, that's the wrong secret key!");  // Print failure message
    return 0;  // Return success
}

/*

00000000004005c5 <main>:
  4005c5:	55                   	push   %rbp
  4005c6:	48 89 e5             	mov    %rsp,%rbp
  4005c9:	48 83 ec 10          	sub    $0x10,%rsp
  4005cd:	89 7d fc             	mov    %edi,-0x4(%rbp)
  4005d0:	48 89 75 f0          	mov    %rsi,-0x10(%rbp)
  4005d4:	83 7d fc 02          	cmpl   $0x2,-0x4(%rbp)
  4005d8:	74 11                	je     4005eb <main+0x26>
  4005da:	bf c8 06 40 00       	mov    $0x4006c8,%edi
  4005df:	e8 0c fe ff ff       	call   4003f0 <puts@plt>
  4005e4:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
  4005e9:	eb 32                	jmp    40061d <main+0x58>
  4005eb:	48 8b 45 f0          	mov    -0x10(%rbp),%rax
  4005ef:	48 83 c0 08          	add    $0x8,%rax
  4005f3:	48 8b 00             	mov    (%rax),%rax
  4005f6:	48 89 c7             	mov    %rax,%rdi
  4005f9:	e8 22 ff ff ff       	call   400520 <verify>
  4005fe:	85 c0                	test   %eax,%eax
  400600:	74 0c                	je     40060e <main+0x49>      // if (v1)
  400602:	bf f0 06 40 00       	mov    $0x4006f0,%edi          // true branch --> we want to reach this
  400607:	e8 e4 fd ff ff       	call   4003f0 <puts@plt>
  40060c:	eb 0a                	jmp    400618 <main+0x53>
  40060e:	bf 18 07 40 00       	mov    $0x400718,%edi           // false branch
  400613:	e8 d8 fd ff ff       	call   4003f0 <puts@plt>
  400618:	b8 00 00 00 00       	mov    $0x0,%eax
  40061d:	c9                   	leave
  40061e:	c3                   	ret
  40061f:	90                   	nop

*/
