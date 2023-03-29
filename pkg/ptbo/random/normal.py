from torch import randn
from torch import Tensor
from ptbo.random.perturbation import Perturbation

class NormalPerturbation(Perturbation):
    def __init__(self, sigma: float = 1.0) -> None:
        self.sigma = sigma

    def sample(self, theta: Tensor, n_samples: int = 1) -> Tensor:
        device = theta.device
        return theta + self.sigma * randn(n_samples, *theta.size(), device=device)

    def dlog(self, theta: Tensor, eta: Tensor) -> Tensor:
        return (eta - theta) / self.sigma ** 2
