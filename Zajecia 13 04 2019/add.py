def add(*args):
    dims = set()

    for m in args:
        len_rows, len_cols = len(m), len(m[0])
        dims.add((len_rows,len_cols))
        len_cols_ = set()
        for row in m:
            len_cols_.add(len(row))
        if len(len_cols_) > 1:
            raise ValueError("Niezgadza sie")
    if len(dims) >1:
        raise ValueError("Niezgadza sie")

    msum=[]

    len_row = len(args[0])
    len_col = len(args[0][0])
    for i in range(len_row):
        row = []
        for j in range(len_col):
            row.append(sum([m[i][j] for m in args]))
        msum.append(row)
    return msum

