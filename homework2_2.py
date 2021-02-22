m_list = input("введите значения списка").split()
print("список", m_list)
ind = len(m_list) if len(m_list) % 2 == 0 else len(m_list) - 1
m_list[:ind:2], m_list[1:ind:2] = m_list[1:ind:2], m_list[:ind:2]
print(m_list)