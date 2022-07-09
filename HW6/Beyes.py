from random import choices


def samples():
    pop = [0, 1]
    # calculates Burgulary
    b_weights = [1-0.001, 0.001]
    e_weights = [1-0.002, 0.002]
    a_weights = []
    j_weights = []
    m_weights = []
    B = choices(pop, b_weights)[0]
    E = choices(pop, e_weights)[0]
    if E and B:
        a_weights = [1-.95, .95]
    elif not E and B:
        a_weights = [1-.94, .94]
    elif E and not B:
        a_weights = [1-.29, .29]
    else:
        a_weights = [1-.001, .001]
    A = choices(pop, a_weights)[0]
    if A:
        j_weights = [1-.9, .9]
    else:
        j_weights = [1-.05, .05]
    J = choices(pop, j_weights)[0]
    if A:
        m_weights = [1-.7, .7]
    else:
        m_weights = [1-.01, .01]
    M = choices(pop, m_weights)[0]
    return [B, E, A, J, M]


if __name__ == "__main__":
    p_EJM = 0.0
    p_JM = 0.0
    sample_size = 10000000
    for _ in range(sample_size):
        temp = samples()
        if (temp[1] and temp[3] and temp[4]):
            p_EJM += 1
        if (temp[3] and temp[4]):
            p_JM += 1
    p_EJM /= sample_size
    p_JM /= sample_size
    p_EJM_JM = 0.0
    if p_JM:
        p_EJM_JM = p_EJM/p_JM
    print(f"p(E, J, M) = {p_EJM}")
    print(f"p(J, M) = {p_JM}")
    print(f"p(E | J, M) = {p_EJM_JM}")
