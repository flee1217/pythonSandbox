import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani


class DubPen:
    def __init__(self):
        self.m1 = 1
        self.m2 = 2
        self.l1 = 2
        self.l2 = 2
        self.g = 9.81
        self.t_init = 0
        self.dt = .01
        self.t_final = 50
        self.t_vec = np.arange(0, self.t_final + self.dt, self.dt)
        self.theta1_init = 5 * np.pi / 4
        self.theta2_init = 3 * np.pi / 4
        self.omega1_init = 0
        self.omega2_init = 0
        self.theta1_vec = np.empty(int(self.t_final / self.dt) + 2)
        self.theta2_vec = np.empty(int(self.t_final / self.dt) + 2)
        self.omega1_vec = np.empty(int(self.t_final / self.dt) + 2)
        self.omega2_vec = np.empty(int(self.t_final / self.dt) + 2)
        # initializing the state vectors
        self.theta1_vec[0] = self.theta1_init
        self.theta2_vec[0] = self.theta2_init
        self.omega1_vec[0] = self.omega1_init
        self.omega2_vec[0] = self.omega2_init
        self.x1 = []
        self.y1 = []
        self.x2 = []
        self.y2 = []

    def eulerInt(self):
        for i in range(1, self.t_vec.size):
            m1 = self.m1
            m2 = self.m2
            l1 = self.l1
            l2 = self.l2
            g = self.g
            dt = self.dt
            dTheta = self.theta2_vec[i - 1] - self.theta1_vec[i - 1]

            self.omega1_vec[i] = self.omega1_vec[i - 1] + ((m2 * l1 * self.omega1_vec[i - 1] ** 2 * np.sin(dTheta) *
                                np.cos(dTheta) + m2 * g * np.sin(self.theta2_vec[i - 1]) * np.cos(dTheta) + m2 * l2 *
                                self.omega2_vec[i - 1] ** 2 * np.sin(dTheta) - (m1 + m2) *
                                (g * np.sin(self.theta1_vec[i - 1]))) /
                                ((m1 + m2) * l1 + m2 * l1 * np.cos(dTheta) ** 2)) *dt

            self.theta1_vec[i] = self.theta1_vec[i - 1] + self.omega1_vec[i] * dt

            self.omega2_vec[i] = self.omega2_vec[i - 1] +\
                                ((-m2 * l2 * self.omega2_vec[i - 1] ** 2 * np.sin(
                                dTheta) * np.cos(dTheta) + (m1 + m2) * (g * np.sin(self.theta1_vec[i - 1]) *
                                np.cos(dTheta) - l1 * self.omega1_vec[i - 1] ** 2 * np.sin(dTheta) - g *
                                np.sin(self.theta2_vec[i - 1]))) / (l2 * (m1 + m2 - m2 * np.cos(dTheta) ** 2))) * dt

            self.theta2_vec[i] = self.theta2_vec[i - 1] + self.omega2_vec[i] * dt

    def plotResults(self):
        plt.plot(self.t_vec, self.theta1_vec)
        plt.plot(self.t_vec, self.theta2_vec)
        plt.plot(self.t_vec, self.omega1_vec)
        plt.plot(self.t_vec, self.omega2_vec)
        plt.xlabel('time (s)')
        plt.ylabel('rad / rad per second (1/s)')
        plt.title('State plot')
        plt.show()

    def run(self, i):
        lsum = (self.l1 + self.l2) * 1.2
        ax = plt.axes(xlim=(-lsum, lsum), ylim=(-lsum,lsum))
        line, = ax.plot([], [], lw=2)
        line.set_data((0,self.x1[i],self.x2[i]),(0,self.y1[i],self.y2[i]))
        # line.set_color('magenta')

        return line,

    def animateResult(self):
        fig = plt.figure()
        print 'got here'
        self.x1, self.y1 = (self.l1 * np.sin(self.theta1_vec), -np.cos(self.theta1_vec) * self.l1)
        self.x2, self.y2 = (self.l2 * np.sin(self.theta2_vec) + self.x1, -np.cos(self.theta2_vec) * self.l2 + self.y1)
        a = ani.FuncAnimation(fig, self.run, frames=len(self.t_vec), interval=0, repeat=False, blit=True)
        plt.show()
        print 'after here'




myDP = DubPen()
myDP.eulerInt()
# myDP.plotResults()
myDP.animateResult()
