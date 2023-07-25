

def combine_terms(terms):
    # Comparing terms and separating those that differ by one bit.
    combined_terms = []
    n = len(terms[0])
    for i in range(len(terms)):
        for j in range(i + 1, len(terms)):
            t1 = terms[i]
            t2 = terms[j]
            diff_count = 0
            combined = ""
            for k in range(n):
                if t1[k] != t2[k]:
                    diff_count += 1
                    combined += "x"
                else:
                    combined += t1[k]
            if diff_count == 1:
                combined_terms.append(combined)
    return combined_terms


def generate_pi(minterms, num_vars):
    # Convert terms into binary form and call combine_terms() to generate PI's.
    prime_implicants = []
    terms = [bin(m)[2:].zfill(num_vars) for m in minterms]
    while True:
        combined_terms = combine_terms(terms)
        if not combined_terms:
            break
        prime_implicants.extend(combined_terms)
        terms = combined_terms
    return prime_implicants


def minimize_boolean_function(minterms, dont_cares, num_vars):
    prime_implicants = generate_pi(minterms + dont_cares, num_vars)
    prime_implicants.sort(key=lambda x: x.count("x"))
    essential_implicants = []
    minimized_expression = ""
    covered_minterms = set()
    for implicant in prime_implicants:
        count = 0
        for minterm in minterms:
            if implicant.replace("x", "0") in bin(minterm)[2:].zfill(num_vars):
                count += 1
                covered_minterms.add(minterm)
        if count == 1:
            essential_implicants.append(implicant)
    for implicant in essential_implicants:
        minimized_expression += implicant.replace(" ", "x")
        minimized_expression += " + "
    if minimized_expression:
        # Remove the trailing " + "
        minimized_expression = minimized_expression[:-3]
    return minimized_expression, list(covered_minterms)


number_of_vars = 3
func_terms = [0, 2, 5]
func_dont_cares = []


expression, covered_terms = minimize_boolean_function(func_terms, func_dont_cares, number_of_vars)

print("Minimized Expression:", expression)
print("Covered Minterms:", covered_terms)
