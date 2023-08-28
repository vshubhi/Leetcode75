def max_sum_sub(nums, max_sum, prev, curr_ind, curr_sum):
    if curr_ind>=len(nums):
        return max(curr_sum, max_sum)

    # pick
    sum_p = -int('-inf')
    if (prev<nums[curr_ind] and curr_sum+nums[curr_ind] > curr_sum):
        sum_p = max_sum_sub(nums, max_sum, nums[curr_ind], curr_ind+1, curr_sum+nums[curr_ind])

    # do not pick
    sum_np = max_sum_sub(nums, max_sum, prev, curr_ind+1, curr_sum)
    return max(sum_p, sum_np)

if __name__ == '__main__':
    arr = [1,8,3,4,5,6]
    max_sum = -int('inf')
    prev = -int('inf')
    for i in range(len(arr)):
        ans = max_sum_sub(arr, max_sum, prev, i, 0)
        max_sum = max(max_sum, ans)
    print(max_sum)

(-inf, 1, 1, 1) X-> (-inf, 1, 2, 1) 3 -> p (-inf, 3, 3, 4) 4-> (-inf, 4, 4, 8) -> (-inf, 5, 5, 13)
-> (-inf, 6, 6, 19)
sum_np = 19 [1]

i = 0 -> max_sum_sub(arr, -inf, -inf, 0, 0) p-> (-inf, 1, 1, 1) -> (-inf, 8, 2,9) -> (-inf, 8, 3, 9) 
-> (-inf, 8, 4, 9) -> (-inf, 8, 5, 9) np -> (-inf, 8, 6, 9)

sum_p = 9 [1]


[0] sum_p =19
[0] sum_np -> max_sum_sub(arr, -inf, -inf, 0, 0) np -> 

(arr, -inf, -inf, 1, 0) -> (-inf, -inf, 2, 8)
-> arr(-inf, -inf, 2, 0)


def modify(func):
    def wrapper(*args, **kwargs):
        print("wrap")
        func()
    return wrapper

@modify
def fun():
    print("fun")

fun()


1. API received audio as input
2. API calls third party API that takes audio as input returns subtitles
 
audio stored in S3
audio_id, username, remarks
service_name > audio_id> original_file> audio
service_name > audio_id> subtitles > subtitle


user uploads file -> API1 1. authorization check, validated input 
                        2. Uploads file to S3 
                        3.Calls API2 for subtitles 

response from API2 1. Gives error > return error
2. Return File with subtitles -> API1 uploads the file in S3 : ervice_name > audio_id> subtitles > subtitle
and return the link to subtitle


class A():
    def run():
        print("A")
class B(A):
      def run():
        print("B")
class C(B):
    def run():
        print("C")

class D(B, C):
     pass

d = D()
d.run()

            