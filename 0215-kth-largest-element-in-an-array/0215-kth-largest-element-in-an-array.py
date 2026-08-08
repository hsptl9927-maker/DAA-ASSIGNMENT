class Solution:
    def findKthLargest(self, a, k):
        p,l,m,r = choice(a),[],[],[]
        for v in a: (m,l,r)[(p<v)-(v<p)].append(v)
        if k<=len(l): return self.findKthLargest(l,k)
        if len(l)+len(m)<k: return self.findKthLargest(r,k-len(l)-len(m))
        return p