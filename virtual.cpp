
#include <iostream>
class brain{
    public:
    virtual void sense(){
    std::cout<<"brain sense something"<<std::endl;
    }
};
class skin : public brain{
    public:
    void sense () override{
        std::cout<<"sense a touch"<<std::endl;
    }
};
int main(){
    skin touch;
    brain* neuron;
    neuron = &touch;
    neuron->sense();
    return 0;
}