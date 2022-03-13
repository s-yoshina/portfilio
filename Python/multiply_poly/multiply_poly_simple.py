class MultiplyPolySimple:
    def calculate_distribution(self, num:int, poly:list) -> list:
        """Conducts multiplication distribution."""
        products = []
        for value in poly:
            products.append(num*value)
        return products

    def add_to_poly(self, products:list, poly:list, order:int):
        """Adds the products to the polynomial."""
        for i, product in enumerate(products):
            poly[order+i] += product

    def multiply_poly(self, poly1:list, poly2:list) -> list:
        """Multiplies two polynomials."""
        # If the inserted polynomial is an empty list.
        if len(poly1) == 0 or len(poly2) == 0:
            return

        # Initialize the polynomial
        poly = [0] * (len(poly1) + len(poly2) - 1)

        for order, num in enumerate(poly1):
            products = self.calculate_distribution(num, poly2)
            self.add_to_poly(products, poly, order)
        return poly

if __name__ == "__main__":
    a = [2,5,3,1,-1] # Represents 2+5x+(3x^2)+(x^3)-(x^4)
    b = [1,2,2,3,6] # Represents 1+2x+(2x^2)+(3x^3)+(6x^4)
    mps = MultiplyPolySimple()
    s = mps.multiply_poly(a,b)
    print(s)