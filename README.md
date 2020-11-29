# Bachelor Thesis: Security Aspects of Container Orchestration

**Author**:         [Patrick Deutschmann](mailto:patrick.deutschmann@student.tugraz.at)

**Advisor**:         [Stefan More](mailto:stefan.more@iaik.tugraz.at), (Peter Lipp)

**Project goals**:   Understand security aspects of Container Orchestration (especially the Kubernetes project). Give recommendations to operators or developers. 

## Abstract

Containerisation is increasingly gaining traction to run modern applications in distributed environments. To run containers on a large scale and with high availability, container orchestration systems are commonly employed. The most widely used container orchestration system today is Kubernetes, which is highly flexible, but also comes with significant complexity.

In this thesis, we analyse the security of Kubernetes architectures. To do so, we create a layer model to give a holistic view of all relevant aspects. We demonstrate how an example application can securely run in a Kubernetes cluster and which configurations are necessary to strengthen security by employing multiple redundant barriers.

Our research shows that most Kubernetes installers already come with reasonably secure default configurations. However, custom adaptations in consideration of the deployed applications and their requirements to the runtime environment are imperative for secure cluster setup.

---

*See full thesis [here](thesis/main.pdf).*