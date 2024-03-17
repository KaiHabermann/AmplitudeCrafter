from AmplitudeCrafter.Nbody import DecayTopology
from AmplitudeCrafter.Nbody.DecayTopology import generateTreeDefinitions, Node, TopologyGroup
from AmplitudeCrafter.ParticleLibrary import particle
from jax import numpy as jnp
from AmplitudeCrafter.Nbody.Decay import NBodyDecay

from jax import config
config.update("jax_enable_x64", True)

p0 = particle.get_particle("B+")
p1 = particle.get_particle("K+")
p2 = particle.get_particle("p")
p3 = particle.get_particle("p~")
p4 = particle.get_particle("pi0")

tg = TopologyGroup(p0, [p1,p2,p3,p4])
assert len(tg.trees) == 15

tg = TopologyGroup(p0, [p1,p2,p3])
assert len(tg.trees) == 3

tg = TopologyGroup(p0, [p1,p2])
assert len(tg.trees) == 1

tg = TopologyGroup(0,[1,2,3,4])
assert len(tg.trees) == 15

tg = TopologyGroup(0,[1,2,3])
assert len(tg.trees) == 3

tg = TopologyGroup(0,[1,2])
assert len(tg.trees) == 1

tg = TopologyGroup(0,[1,2,3,4,5])
assert len(tg.trees) == 105


decay = NBodyDecay(0,1,2,3,4, 5)

momenta = {   1: jnp.array([0, 0, -0.9, 1]),
              2: jnp.array([0, 0.15, 0.4,1]),
              3: jnp.array([ 0, 0.3, 0.3,1]),
              4: jnp.array([ 0, 0.1, 0.4,1]),
              5: jnp.array([ 0, 0.1, 0.8,1])}

momenta = tg.trees[0].to_rest_frame(momenta)
first_node = tg.trees[0].inorder()[0]
tree = tg.trees[0]
# print(first_node.value ,first_node.momentum(momenta))
# exit(0)
print(tree.boost(Node(4), momenta).decode())
# print(first_node.boost(first_node, momenta)
exit(0)
for node in tg.filter(Node((2,1,3)), Node((1,2))) :
    # print(node.print_tree())
    print(node)    
