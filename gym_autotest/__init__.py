from gym.envs.registration import register

register(id='autotest-v1',
         entry_point='gym_autotest.envs:autotestEnv',
         )