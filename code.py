class Solution:
    def flatten(self, head):
        if not head: return None
        stack = [head]; p = None
        while stack:
            r = stack.pop()
            if p:
                p.next,r.prev = r,p
            p = r
            if r.next:
                stack.append(r.next)
            if r.child:
                stack.append(r.child)
                r.child = None
        return head

              
