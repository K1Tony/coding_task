def prime(n: int) -> bool:
    if n < 2: return False

    divisor = 2
    while divisor <= n ** 0.5:
        if n % divisor == 0: return False

        if divisor == 2:
            divisor += 1
        else:
            divisor += 2
    
    return True


def sequences(seq_a: list[int], seq_b: list[int]) -> list[int]:
    seq_c = []
    for i in seq_a:
        start, end = 0, len(seq_b) - 1
        counter = 0

        while start < end:
            if seq_b[start] == i:
                counter += 1
            if seq_b[end] == i:
                counter += 1
            start += 1
            end -= 1
        
        if start == end and seq_b[start] == i:
            counter += 1
        
        if not prime(counter):
            seq_c.append(i)
    
    return seq_c
