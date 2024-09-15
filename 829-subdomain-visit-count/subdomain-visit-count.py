class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hm = {}
        sol = []

        for domain in cpdomains:
            domainList = domain.split()[1].split(".")
            for index in range(len(domainList)):
                subdomain = ".".join(domainList[index:len(domainList)])
                if subdomain in hm:
                    hm[subdomain] += int(domain.split()[0])
                else:
                    hm[subdomain] = int(domain.split()[0])

        for domain, visits in hm.items():
            sol.append(f"{visits} {domain}")
        return sol