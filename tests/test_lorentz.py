from AmplitudeCrafter.Nbody.kinematics import *
from AmplitudeCrafter.Nbody.lorentz import LorentzTrafo
from jax import numpy as jnp
import jax
import numpy as np

jax.config.update("jax_enable_x64", True)
def test_lotentz():
    m = 139.57018 # MeV
    p = jnp.array([-400., 0, 0])
    P = jnp.array([*p, (m**2 + jnp.sum(p**2))**0.5])

  
    psi, theta, xi, theta_rf, phi_rf, psi_rf = -1.8, 1.3, 1.4, 1.5, 2.6, -2.1 + 2* np.pi
    M = build_4_4(psi, theta, xi, theta_rf, phi_rf, psi_rf)


    M2 = build_2_2(psi, theta, xi, theta_rf, phi_rf, psi_rf)
    trafo = LorentzTrafo(psi, theta, xi, theta_rf, phi_rf, psi_rf)
    psi_, theta_, xi_, theta_rf_, phi_rf_, psi_rf_ = trafo.decode()

    assert np.allclose(M, build_4_4(psi_, theta_, xi_, theta_rf_, phi_rf_, psi_rf_))

    assert np.allclose(psi, psi_)
    assert np.allclose(theta, theta_)
    assert np.allclose(xi, xi_)
    assert np.allclose(phi_rf, phi_rf_)
    assert np.allclose(theta_rf, theta_rf_)
    assert np.allclose(psi_rf, psi_rf_)



if __name__ == "__main__":
    test_lotentz()