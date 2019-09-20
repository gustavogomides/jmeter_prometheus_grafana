
class CalculatorBusiness:
    @classmethod
    def solve_quadratic_equation(cls, body):
        a = float(body.get('a', 0))
        b = float(body.get('b', 0))
        c = float(body.get('c', 0))

        delta = (b**2) - (4*a*c)
        if delta < 0:
            return {
                'message': 'Essa função não apresenta uma raiz real!',
                'delta': delta,
                'success': False
            }

        x1 = (-b + delta**(1.0/2.0)) / (2.0*a)
        x2 = (-b - delta**(1.0/2.0)) / (2.0*a)

        return {
            'x1': x1,
            'x2': x2,
            'message': 'OK',
            'success': True
        }
