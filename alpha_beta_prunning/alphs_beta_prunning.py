MIN=float("-inf")
MAX=float("inf")
def alpha_beta(depth, index, maximizingPlayer,values, alpha, beta):
    if depth == 0:
        return values[index]


    if maximizingPlayer:
        opti = MIN
        for i in range(0, 2):
            val = alpha_beta(depth - 1, index * 2 + i,False, values, alpha, beta)
            opti = max(opti, val)
            alpha = max(alpha, opti)
            if beta <= alpha:
             break
        return opti

    else:
        opti = MAX
        for i in range(0, 2):
          val = alpha_beta(depth - 1, index * 2 + i,True, values, alpha, beta)
          opti = min(opti, val)
          beta = min(beta, opti)
          if beta <= alpha:
            break
        return opti


# Driver Code
if __name__ == "__main__":


    values = [10,5,7,11,12,8,9,8,5,12,11,12,9,8,7,10]
    dep=int(np.log2(len(values)))
    print("The value is :", alpha_beta(dep, 0, True, values, MIN, MAX))