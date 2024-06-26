import React from "react";
import styled from "styled-components"

const Card = styled.div`
    width: 100%;
    border-top: 2px solid ${({ theme }) => theme.text_secondary + 60};
    padding: 10px 0px 0px 0px;
    height: 140px;
    display: flex;
    flex-direction: column;
    background: white;
    gap: 16px;
    color: black;
    `;

const Details = styled.div`
    display: flex;
    flex-direction: column;
    padding: 4px 2px;
    flex: 1;
`;

const Button = styled.div`
    display: flex;
    width: 150px;
    border-radius: 2px;
    padding: 10px;
    flex-wrap: wrap;
    gap: 24px;
    justify-content: center;
    background: black;
    color: white;
    font-weight: 400;
    &:hover {
        opacity: 0.7;
        cursor: pointer;
        }
    `;

const Price = styled.div`
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 18px;
    font-weight: 500;
    color: ${({ theme }) => theme.text_primary};
    margin-bottom: 7px;
    `;

const Size = styled.div`
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 14px;
    font-weight: 500;
    color: black;
    margin-bottom: 10px;
    `;

const Span2 = styled.div`
    
    color: black;
    font-size: 16px;
    
    `;

const Span = styled.div`
    font-size: 22px;
    font-weight: 500;
    color: ${({ theme }) => theme.text_secondary + 60};
    text-decoration: line-through;
    text-decoration-color: ${({ theme }) => theme.text_secondary + 50};
    `;

const Store = styled.div`
    font-size: 15px;
    font-weight: 600;
    color: ${({ theme }) => theme.text_primary};
    margin-bottom: 10px;
    `;

const Percent = styled.div`
    font-size: 16px;
    font-weight: 500;
    color: green;
    `;

const RecommerceCard = ({recommerceProduct}) => {

    //useEffect(() => {}, []);
    return <Card>
        <Details>
            <Store>{recommerceProduct?.store}</Store>
            <Price>{recommerceProduct?.price} 
                <Percent>{recommerceProduct?.percent_off}% off</Percent>
            </Price>
            <Size>Size <Span2>{recommerceProduct?.size}</Span2></Size> 
            <Button onClick={() => {
                window.open(recommerceProduct?.link)
            }}>Buy Now</Button> 
        </Details>
    </Card>
};

export default RecommerceCard;

