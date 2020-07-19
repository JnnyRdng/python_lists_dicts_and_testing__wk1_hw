# Weekend homework for week_01
## Manipulating dictionaries and lists

This homework required us to write functions in `pet_shop.py` that would pass the tests in `pet_shop_test.py`. The tests presented a variety of data structures that would need to be manipulated to find the answer that would satisfy the test.

___

>## Example:
>
>in `pet_shop_test.py`:
>```python
>    def test_total_cash(self):
>        sum = get_total_cash(self.cc_pet_shop)
>        self.assertEqual(1000, sum)
>```
>where the `cc_pet_shop` dictionary is:
>```python
>self.cc_pet_shop = {
>            "pets": [
>                {
>                    "name": "Sir Percy",
>                    "pet_type": "cat",
>                    "breed": "British Shorthair",
>                    "price": 500
>                }
>            ],
>            "admin": {
>                "total_cash": 1000,
>                "pets_sold": 0,
>            },
>            "name": "Camelot of Pets"
>        }
>```
>
>
>In `pet_shop.py` a function `get_total_cash()` needs to be written, taking `cc_pet_shop` as an argument and returning the `"total_cash"` value:
>```python
>def get_total_cash(pet_shop):
>    return pet_shop["admin"]["total_cash"]
>```
> 
>
>
 ___

Successfully completing all 23 tests will result in the following output when running `run_tests.py`:
```
.......................
----------------------------------------------------------------------
Ran 23 tests in 0.001s

OK
```