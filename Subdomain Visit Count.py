class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        subdomains = {}

        for domain in cpdomains:
            rep , d = map(str,domain.split())
            rep = int(rep)
            d = d.split(".")
            for i in range(len(d)):
                subdomain = ".".join(d[i:])
                if subdomain in subdomains:
                    subdomains[subdomain] +=rep
                else:
                    subdomains[subdomain] = rep
        ans = []
        for domain,rep in subdomains.items():
            subdomain = str(rep) + " " + domain
            ans.append(subdomain)
        return ans
