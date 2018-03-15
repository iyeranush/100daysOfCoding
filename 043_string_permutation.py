"""
No duplicates
"""
def string_permutation(string):
    temp_string = [c for c in string]
    permutate(temp_string, 0)

def permutate(string, index):
    if index == len(string):
        print(string)
        return
    for i in range(index, len(string)):
        swap(string, index, i)
        permutate(string, index+1)
        swap(string, index, i)

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

string_permutation("abc")
"""
void permutate( char[] str, int index )
{
    int i = 0;
    if( index == strlen(str) )
    { // We have a permutation so print it
        printf(str);
        return;
    }
    for( i = index; i < strlen(str); i++ )
    {
        swap( str[index], str[i] ); // It doesn't matter how you swap.
        permutate( str, index + 1 );
        swap( str[index], str[i] );
    }
} permutate( "abcdefgh", 0 );




def permutate(string1, index)
    i = 0
    last_char = 0
    if(index == len(string1))
        print(string1)
        return
    permutate( string1, index + 1 );
    lastChar = string1[index];
    for( i = index + 1; i < strlen(str); i++ )
        if(lastChar == str[i]):
            continue
        else:
            lastChar = str[i]
        swap( str[index], str[i] )
        permutate( str, index + 1 )
        swap( str[index], str[i] )
"""
