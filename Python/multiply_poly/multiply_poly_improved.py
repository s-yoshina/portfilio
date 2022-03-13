class MultiplyPolyImproved:
    def resize_poly(self, poly:list, length:int) -> list:
        """Resizes a polynomial to a given length using zeros."""
        return poly + [0]*length

    def calculate_order(self,poly1_len:int, poly2_len:int) -> int:
        """Calculates the order of the added polynomial."""
        order = (poly1_len+poly2_len-2)//2
        if order % 2 != 0:
            order += 1
        return order

    def split_poly(self, poly:list) -> (list,list):
        """Splits a polynimal into half."""
        split_index = len(poly)//2
        a0 = poly[:split_index]
        a1 = poly[split_index:]
        return a0, a1

    def add_poly(self, poly1: list, poly2: list) -> list:
        """Adds two polynomials ordered from the lowest to the
        highest order and returns the sum as a list."""
        added_poly = []
        p1_i = 0
        p2_i = 0
        while p1_i < len(poly1) or p2_i < len(poly2):
            if p1_i < len(poly1) and p2_i < len(poly2):
                added_poly.append(poly1[p1_i]+poly2[p2_i])
                p1_i += 1
                p2_i += 1
            elif p1_i < len(poly1):
                added_poly.append(poly1[p1_i])
                p1_i += 1
            elif p2_i < len(poly2):
                added_poly.append(poly2[p2_i])
                p2_i += 1
        return added_poly

    def increase_order(self, poly:list, order:int) -> list:
        """Increase the order of a polynomial to the given order."""
        return [0]*order + poly

    def multiply_poly(self, poly1:list, poly2:list) -> list:
        """Multiplies two polynomials. The polynomials entered must be ordered
           from lowest to highest order."""

        # Resize polynomial if lengths don't match.
        if len(poly1) > len(poly2):
            poly2 = self.resize_poly(poly2, len(poly1)-len(poly2))
        elif len(poly2) > len(poly1):
            poly1 = self.resize_poly(poly1, len(poly2)-len(poly1))

        # If both polynomials are a constant
        if len(poly1) == 1:
            return [poly1[0]*poly2[0]]
        order = self.calculate_order(len(poly1),len(poly2))

        # Split the polynomials into halves
        a0, a1 = self.split_poly(poly1)
        b0, b1 = self.split_poly(poly2)

        # Obtain components
        y = self.multiply_poly(self.add_poly(a0,a1),self.add_poly(b0,b1))
        u = self.multiply_poly(a0,b0)
        z = self.multiply_poly(a1,b1)

        # Multiply components
        neg_u = [-1*i for i in u]
        neg_z = [-1*i for i in z]
        sum1 = self.add_poly(self.add_poly(y,neg_u),neg_z)
        comp1 = self.increase_order(sum1, order//2)
        comp2 = self.increase_order(z, order)
        return self.add_poly(self.add_poly(u,comp1), comp2)

if __name__ == "__main__":
    a = [2,5,3,1,-1] # Represents 2+5x+(3x^2)+(x^3)-(x^4)
    b = [1,2,2,3,6] # Represents 1+2x+(2x^2)+(3x^3)+(6x^4)
    mpi = MultiplyPolyImproved()
    s = mpi.multiply_poly(a,b)
    print(s)