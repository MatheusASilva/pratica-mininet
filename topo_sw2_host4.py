
"""
Custom topology for:
2 switches and 4 hosts

   h1     h2
    \     /
     s1--s2
    /     \
  h3       h4

Command to run:
sudo mn --custom topo_sw2_host4.py --topo sw2host4 --link tc,bw=10
"""

from mininet.topo import Topo

class Sw2Host4(Topo):
    def build(self):

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Connect hosts to switches
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

        self.addLink(h4, s2)

        # Connect the switches
        self.addLink(s1, s2)

# Required so Mininet can find the topology
topos = {"sw2host4": (lambda: Sw2Host4())}
